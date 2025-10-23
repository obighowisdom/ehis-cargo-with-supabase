# core/middleware.py

from django.http import HttpResponse
from django.conf import settings

class MaintenanceModeMiddleware:
    """
    Middleware to display a maintenance message when MAINTENANCE_MODE is True.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip for admin or superuser (optional)
        if getattr(settings, "MAINTENANCE_MODE", False):
            if request.path.startswith("/admin/"):
                return self.get_response(request)

            return HttpResponse(
                """
                <html>
                    <head>
                        <title>Maintenance</title>
                        <style>
                            body {
                                display: flex;
                                justify-content: center;
                                align-items: center;
                                height: 100vh;
                                font-family: Arial, sans-serif;
                                background: #f7f8fa;
                            }
                            .message {
                                text-align: center;
                                background: white;
                                padding: 40px;
                                border-radius: 16px;
                                box-shadow: 0 2px 12px rgba(0,0,0,0.1);
                            }
                            h1 {
                                color: #444;
                                margin-bottom: 10px;
                            }
                            p {
                                color: #777;
                            }
                        </style>
                    </head>
                    <body>
                        <div class="message">
                            <h1>🛠️ Maintenance Ongoing</h1>
                            <p>We’re currently performing scheduled maintenance.<br>
                            Please check back soon.</p>
                        </div>
                    </body>
                </html>
                """,
                content_type="text/html",
                status=503,
            )

        return self.get_response(request)
