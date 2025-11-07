import docker

client = docker.from_env()
image_name = "falkordb/falkordb:latest"
ports = {
    '6379/tcp': 6379,
    '3000/tcp': 3000
}
container_name_prefix = "falkordb_instance"

def is_container_running(image_name_check):
    """Checks if any container based on the given image name is already running."""
    # List all running containers
    for container in client.containers.list():
        # Check if the container's image tag matches our target image name
        # We check tags explicitly because `container.image.tags` is a list
        if image_name_check in container.image.tags:
            print(f"Found existing running container: {container.name} (ID: {container.short_id})")
            return container
    return None

def run_falkordb():
    running_container = is_container_running(image_name)

    if running_container:
        print(f"Container is already running. Skipping startup.")
        # You can add logic here to interact with the existing container if needed.
    else:
        print("No existing container found for this image. Starting a new one...")
        try:
            # Pull the image if not already present
            print(f"Ensuring image {image_name} is available...")
            client.images.pull(image_name)
            
            # Run the new container
            container = client.containers.run(
                image_name,
                ports=ports,
                remove=True,  # Automatically removes container when stopped
                detach=True   # Runs in the background
            )
            print(f"New container started successfully with ID: {container.id}")
            print(f"Access Redis/FalkorDB on localhost:6379 and UI on localhost:3000")

        except docker.errors.ImageNotFound:
            print(f"Error: Image '{image_name}' not found. Please ensure it is available.")
        except docker.errors.APIError as e:
            print(f"Docker API error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

