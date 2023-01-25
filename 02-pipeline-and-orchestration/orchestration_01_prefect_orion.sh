# Resource : https://docs.prefect.io/tutorials/orion/

# start a local prefect API server :
# server runs locally at : http://127.0.0.1:4200.
prefect orion start

# Set the PREFECT_API_URL for your server
# Makes sure that you're coordinating flows with the correct API instance
prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api

# Navigate through the prefect api DOC
# Swagger :
SWAGGER_URL=http://127.0.0.1:4200/docs
# Redoc :
REDOC_URL=http://127.0.0.1:4200/redoc

# Prefect database :
LOCAL_DB='~/.prefect/orion.db'

# Change database (sqlite example) :
export PREFECT_ORION_DATABASE_CONNECTION_URL="sqlite+aiosqlite:////full/path/to/a/location/orion.db"

# Delete flows runs & other prefect artifacts from database :
prefect orion database reset
