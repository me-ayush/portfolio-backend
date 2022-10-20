from django.contrib import admin
from .models import *
from django.utils.html import format_html


class CertificateAdmin(admin.ModelAdmin):
    list_display = ("id","certificate_name","link","certificate_issuer", "issue_date", "action")
    # list_display_links = ("id","certificate_name")
    list_display_links = None

    def action(self, obj):
        return format_html(
                '<a href="{0}/change">Edit</a> <a href="{0}/delete">Delete</a>',
                obj.id,
            )

    def issue_date(self, obj):
        return f"{obj.certificate_issue_year}/{obj.certificate_issue_month}/{obj.certificate_issue_date}"

    def link(self, obj):
        return format_html(
                '<a href="{0}" target="_blank">{1}</a>',
                obj.certificate_link,
                obj.certificate_link,
            )


# Register your models here.
admin.site.register(Certificates, CertificateAdmin)