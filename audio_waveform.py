def generate_waveform_html(audio_filename: str) -> str:
    audio_url = f"/static/audio/{audio_filename}"
    return f"""
    <div id="player-container" style="display: flex; flex-direction: column; align-items: flex-start; gap: 1rem;">
        <audio id="audioElem" controls src="{audio_url}"></audio>
        <canvas id="canvasElem" width="500" height="100"></canvas>
    </div>

    <script src="https://unpkg.com/@foobar404/wave"></script>
    <script>
        function initWaveform() {{
            const audioElement = document.getElementById("audioElem");
            const canvasElement = document.getElementById("canvasElem");

            if (!audioElement || !canvasElement) {{
                console.error("Missing audio or canvas element!");
                return;
            }}

            const wave = new Wave();
            wave.fromElement(audioElement, canvasElement, {{
                type: "bars",
                colors: ["#6a0dad", "#8f00ff"],
                stroke: 1,
            }});
        }}

        if (document.readyState !== "loading") {{
            initWaveform();
        }} else {{
            document.addEventListener("DOMContentLoaded", initWaveform);
        }}
    </script>
    """
