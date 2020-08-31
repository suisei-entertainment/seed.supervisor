
## ============================================================================
##                   **** SEED Virtual Reality Platform ****
##                Copyright (C) 2019-2020, Suisei Entertainment
## ============================================================================
##
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.
##
## ============================================================================

# Use Ubuntu 20.04 LTS as the base image
ARG BASE_IMAGE=ubuntu:20.04
FROM $BASE_IMAGE

MAINTAINER Suisei Entertainment <info@suiseientertainment.com>

# Set the working directory
WORKDIR .

# Copy files to the image filesystem
COPY ./dist/seed.supervisor .

# Expose port 11492 in the container
EXPOSE 11492

# Start the supervisor daemon
CMD ["seed.supervisor", "start"]
