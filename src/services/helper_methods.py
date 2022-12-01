def get_full_url(domain, target_site):
    if domain.endswith('/') and target_site.startswith('/'):
        return domain + target_site[1:]
    elif not domain.endswith('/') and not target_site.startswith('/'):
        return f"{domain}/{target_site}"
    else:
        return domain + target_site
