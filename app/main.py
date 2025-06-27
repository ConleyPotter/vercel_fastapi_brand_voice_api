# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class BrandVoiceRequest(BaseModel):
    brand_essence: str
    core_metaphor: str
    voice_adjectives: List[str]
    voice_boundaries: str
    tone_sliders: str
    core_values: List[str]
    values_in_action: str
    recurring_themes: List[str]
    audience_mirror: str
    visual_influences: str = ""

@app.post("/api/generate-voice-primer")
def generate_voice_primer(data: BrandVoiceRequest):
    adjectives_str = ", ".join(data.voice_adjectives)
    values_str = ", ".join(data.core_values)
    themes_str = ", ".join(data.recurring_themes)

    primer = f"""This brand exists to {data.brand_essence}. It can be described as {adjectives_str}, with a tone that lives somewhere between {data.tone_sliders}. Imagine it speaking in a voice that feels like {data.core_metaphor}.

Its values include {values_str}, and one of those values shows up as: {data.values_in_action}.

Themes that recur in their work include: {themes_str}. They speak to an audience who can be described as: {data.audience_mirror}.

Avoid using language that feels {data.voice_boundaries}. Instead, lean into the emotional atmosphere created by {data.core_metaphor} and the stylistic influences of {data.visual_influences}.

When generating content, echo this brand's inner voice: present, honest, and aligned with their emotional values."""

    return {"brand_voice_primer": primer}
