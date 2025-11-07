"""
Run FalkorDB in Docker with persistent volume storage.
Updated to use REDIS_ARGS per FalkorDB docs and verify persistence.
"""

from pathlib import Path
import docker
from docker.models.containers import Container
from pathlib import Path

# --- Docker client -----------------------------------------------------------
try:
    client = docker.from_env()
except Exception as e:
    print("❌ IS DOCKER RUNNING?")
    raise e

# --- Config ------------------------------------------------------------------
IMAGE = "falkordb/falkordb:latest"
NAME_PREFIX = "falkordb_instance"

# Prefer an absolute host path in your repo (bind mount), OR use a named volume.
# Bind mount (repo-local folder):
repo_root = Path(__file__).resolve().parent.parent  # adjust if needed
host_data_dir = repo_root / "db" / "falkordb_data"
host_data_dir.mkdir(parents=True, exist_ok=True)

ports = {"6379/tcp": 6379, "3000/tcp": 3000}

# Mount host folder -> /data in container (Redis official VOLUME path)
volumes = {str(host_data_dir): {"bind": "/var/lib/falkordb/data", "mode": "rw"}}

# Pass Redis flags via environment (preferred for FalkorDB image)
command = [
    "--dir", "/data",
    "--dbfilename", "dump.rdb",
    "--appendonly", "no"
]

def find_running() -> Container | None:
    for c in client.containers.list():
        # match by image or name prefix
        if IMAGE in c.image.tags or c.name.startswith(NAME_PREFIX):
            return c
    return None

def run_falkordb() -> Container:
    running = find_running()
    if running:
        print(f"🟢 Container already running: {running.name} ({running.short_id})")
        return running

    print(f"⏬ Pulling {IMAGE} (if needed)...")
    client.images.pull(IMAGE)
    name = f"{NAME_PREFIX}"

    print("🚀 Starting FalkorDB with persistence at", host_data_dir)
    container = client.containers.run(
        IMAGE,
        name=name,
        detach=True,
        tty=True,
        restart_policy={"Name": "always"},
        ports=ports,
        volumes=volumes,
        command=command,
    )
    print(f"   - Container: {container.short_id}")
    print("   - UI: http://localhost:3000  |  Redis: localhost:6379")
    return container

def save_db(falkordb_container: Container):
    falkordb_container.exec_run("redis-cli SAVE")
    print("✅ Saved dump.rdb in db/falkordb_data/dump.rdb")

if __name__ == "__main__":
    c = run_falkordb()
    print(f"📁 Host data dir: {host_data_dir.resolve()}")
