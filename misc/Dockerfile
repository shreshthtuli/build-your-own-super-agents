# Use Debian Slim with Node.js 23 as base image
FROM node:23-slim

# Set working directory
WORKDIR /app

# Install git and other necessary tools
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Clone the Pokemon Showdown repository
RUN git clone https://github.com/smogon/pokemon-showdown.git .

# Copy the example config to config.js (as mentioned in README)
RUN cp config/config-example.js config/config.js

# Configure server to bind to all interfaces (0.0.0.0) for Docker
# This adds the bindaddress setting if it doesn't exist, or modifies it if it does
RUN if grep -q "bindaddress" config/config.js; then \
        sed -i "s/exports\.bindaddress = .*/exports.bindaddress = '0.0.0.0';/" config/config.js; \
    else \
        echo "exports.bindaddress = '0.0.0.0';" >> config/config.js; \
    fi

# Accept build argument for admin username (defaults to "admin")
ARG ADMIN_USER=admin

# Create usergroups.csv with admin user
RUN echo "$ADMIN_USER,~" > config/usergroups.csv && \
    echo "Admin user set: $ADMIN_USER"

# Install dependencies and build
RUN npm install

# Expose the default Pokemon Showdown port
EXPOSE 8000

# Create a non-root user for security
RUN groupadd -r showdown && useradd -r -g showdown showdown
RUN chown -R showdown:showdown /app
USER showdown

# Start the server (using the recommended method from README with explicit port)
CMD ["node", "pokemon-showdown", "8000", "--no-security"]