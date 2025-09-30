# -----------------------------
# Stage 1: Build React/TS app
# -----------------------------
FROM node:20-bookworm AS build

# Set working directory and copy package files and install dependencies
WORKDIR /web
COPY package*.json ./
RUN npm install

# Copy the rest of the frontend source code
COPY . .

# Build the React app for production
RUN npm run build

# -----------------------------
# Stage 2: Run with lightweight web server
# -----------------------------
FROM nginx:alpine

# Copy built frontend from build stage into Nginx html dir
COPY --from=build /web/dist /usr/share/nginx/html

# Expose frontend port
EXPOSE 80

# Nginx serves static frontend files
CMD ["nginx", "-g", "daemon off;"]
