import os
from flask import Flask, render_template
from supabase import create_client, Client
from dotenv import load_dotenv


def create_app(test_config=None):
    app = Flask(__name__)

    supabase: Client = create_client(
    os.environ.get("SUPABASE_URL"),
    os.environ.get("SUPABASE_KEY")
)
    if test_config is not None:
        app.config.from_mapping(test_config)

    from items import bp

    app.register_blueprint(bp)

    @app.get("/")
    def index():
        response = supabase.table('Goals').select("*").execute()
        goals = response.data
        return goals

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
