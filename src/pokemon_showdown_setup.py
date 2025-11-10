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

IMAGE = "shreshthtuli/pokemon-showdown"
NAME_PREFIX = "pokemon-showdown"

def find_running() -> Container | None:
    for c in client.containers.list():
        # match by image or name prefix
        if IMAGE in c.image.tags or c.name.startswith(NAME_PREFIX):
            return c
    return None

def run_pokemon_showdown() -> Container:
    running = find_running()
    if running:
        print(f"🟢 Container already running: {running.name} ({running.short_id})")
        return running

    print(f"⏬ Pulling {IMAGE} (if needed)...")
    client.images.pull(IMAGE)
    name = f"{NAME_PREFIX}"

    print("🚀 Starting Pokemon Showdown...")
    container = client.containers.run(
        IMAGE,
        name=name,
        detach=True,
        tty=True,
        restart_policy={"Name": "always"},
        ports={"8000/tcp": 8000},
    )
    print(f"   - Container: {container.short_id}")
    print("   - UI: http://localhost:8000 ")
    return container
