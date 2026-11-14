
"""Enabled image models for the personal Z-Image-Turbo API."""

from .models.z_image.deployment import deployment as z_image

# Only deploy Z-Image-Turbo for this personal API.
MODEL_DEPLOYMENTS = (z_image,)
