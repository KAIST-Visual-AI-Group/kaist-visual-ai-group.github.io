---
hide:
  - navigation
  - toc
---


# Courses

{% for year in courses.years %}

## {{ year.year }}

<div class="grid cards" markdown>
{% for course in year.courses %}
-   {% if course.link %}<a href="{{ course.link }}" target=_blank>__{{ course.title }}__ ({{ course.time }})</a>{% else %}__{{ course.title }}__ ({{ course.time }}){% endif %}

    ---

    {% if course.desc %}{{ course.desc }}{% endif %}
{% endfor %}
</div>

{% endfor %}
<br>
