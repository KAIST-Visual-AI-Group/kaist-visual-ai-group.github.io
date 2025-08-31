---
hide:
  - navigation
  - toc
---


<style>
.members-thumbnail-cell {
    display: inline-table;
    padding-right: 12px;
    vertical-align: top;
    p { margin: 0px; }
}

.members-description-cell {
    display: inline-table;
    vertical-align: top;
    p { margin: 0px; }
}

.members-thumbnail {
    width: 80px;
    border-radius: 50%;
    -moz-background-clip: padding;
    -webkit-background-clip: padding-box;
    background-clip: padding-box
}
</style>


# Members

## Professor

<div class="grid" markdown>

{% set item = members.professor %}
<div class="card" markdown>
<div class="members-thumbnail-cell" markdown>
<img class="members-thumbnail" src="../assets/profile/{{ item.name }}.png" markdown>
</div>
<div class="members-description-cell" markdown>
{% if item.web %}<a href="{{ item.web }}" target="_blank">__{{ item.name }}__</a>{% else %}__{{ item.name }}__{% endif %}<br>
{{ item.type }}<br>
{% if item.web %}<a href="{{ item.web }}" target="_blank">:fontawesome-solid-house:</a>&nbsp; {% endif %}{% if item.email %}<a href="mailto:{{ item.email }}" target="_top">:fontawesome-solid-envelope:</a>&nbsp; {% endif %}{% if item.twitter %} <a href="{{ item.twitter }}" target="_blank">:fontawesome-brands-x-twitter:</a>&nbsp; {% endif %}{% if item.linkedin %} <a href="{{ item.linkedin }}" target="_blank">:fontawesome-brands-linkedin:</a>&nbsp; {% endif %}{% if item.github %} <a href="{{ item.github }}" target="_blank">:fontawesome-brands-github:</a>&nbsp; {% endif %}{% if item.cv %} <a href="{{ item.cv }}" target="_blank">:academicons-cv:</a>&nbsp; {% endif %}
</div>
</div>

</div>


## Ph.D. Students

<div class="grid" markdown>

{% for item in members.phd %}
<div class="card" markdown>
<div class="members-thumbnail-cell" markdown>
<img class="members-thumbnail" src="../assets/profile/{{ item.name }}.png" markdown>
</div>
<div class="members-description-cell" markdown>
{% if item.web %}<a href="{{ item.web }}" target="_blank">__{{ item.name }}__</a>{% else %}__{{ item.name }}__{% endif %}<br>
{{ item.type }}<br>
{% if item.web %}<a href="{{ item.web }}" target="_blank">:fontawesome-solid-house:</a>&nbsp; {% endif %}{% if item.email %}<a href="mailto:{{ item.email }}" target="_top">:fontawesome-solid-envelope:</a>&nbsp; {% endif %}{% if item.twitter %} <a href="{{ item.twitter }}" target="_blank">:fontawesome-brands-x-twitter:</a>&nbsp; {% endif %}{% if item.linkedin %} <a href="{{ item.linkedin }}" target="_blank">:fontawesome-brands-linkedin:</a>&nbsp; {% endif %}{% if item.github %} <a href="{{ item.github }}" target="_blank">:fontawesome-brands-github:</a>&nbsp; {% endif %}{% if item.cv %} <a href="{{ item.cv }}" target="_blank">:academicons-cv:</a>&nbsp; {% endif %}
</div>
</div>
{% endfor %}

</div>


## Master's Students

<div class="grid" markdown>

{% for item in members.master %}
<div class="card" markdown>
<div class="members-thumbnail-cell" markdown>
<img class="members-thumbnail" src="../assets/profile/{{ item.name }}.png" markdown>
</div>
<div class="members-description-cell" markdown>
{% if item.web %}<a href="{{ item.web }}" target="_blank">__{{ item.name }}__</a>{% else %}__{{ item.name }}__{% endif %}<br>
{{ item.type }}<br>
{% if item.web %}<a href="{{ item.web }}" target="_blank">:fontawesome-solid-house:</a>&nbsp; {% endif %}{% if item.email %}<a href="mailto:{{ item.email }}" target="_top">:fontawesome-solid-envelope:</a>&nbsp; {% endif %}{% if item.twitter %} <a href="{{ item.twitter }}" target="_blank">:fontawesome-brands-x-twitter:</a>&nbsp; {% endif %}{% if item.linkedin %} <a href="{{ item.linkedin }}" target="_blank">:fontawesome-brands-linkedin:</a>&nbsp; {% endif %}{% if item.github %} <a href="{{ item.github }}" target="_blank">:fontawesome-brands-github:</a>&nbsp; {% endif %}{% if item.cv %} <a href="{{ item.cv }}" target="_blank">:academicons-cv:</a>&nbsp; {% endif %}
</div>
</div>
{% endfor %}

</div>


## Undergraduate Students

<div class="grid" markdown>
{% for item in members.undergrads %}
<div class="card" markdown>
{% if item.email %}
<div class="members-thumbnail-cell" markdown>
<img class="members-thumbnail" src="../assets/profile/{{ item.name }}.png" markdown>
</div>
<div class="members-description-cell" markdown>
{% if item.web %}<a href="{{ item.web }}" target="_blank">__{{ item.name }}__</a>{% else %}__{{ item.name }}__{% endif %}<br>
{{ item.type }}<br>
{% if item.web %}<a href="{{ item.web }}" target="_blank">:fontawesome-solid-house:</a>&nbsp; {% endif %}{% if item.email %}<a href="mailto:{{ item.email }}" target="_top">:fontawesome-solid-envelope:</a>&nbsp; {% endif %}{% if item.twitter %} <a href="{{ item.twitter }}" target="_blank">:fontawesome-brands-x-twitter:</a>&nbsp; {% endif %}{% if item.linkedin %} <a href="{{ item.linkedin }}" target="_blank">:fontawesome-brands-linkedin:</a>&nbsp; {% endif %}{% if item.github %} <a href="{{ item.github }}" target="_blank">:fontawesome-brands-github:</a>&nbsp; {% endif %}{% if item.cv %} <a href="{{ item.cv }}" target="_blank">:academicons-cv:</a>&nbsp; {% endif %}
</div>
{% else %}
<div class="members-thumbnail-cell" markdown>
</div>
<div class="members-description-cell" markdown>
__{{ item.name }}__
</div>
{% endif %}
</div>
{% endfor %}
</div>


## Former Graduate Students

<div class="grid" markdown>

{% for item in members.former_graduates %}
<div class="card" markdown>
<div class="members-thumbnail-cell" markdown>
<img class="members-thumbnail" src="../assets/profile/{{ item.name }}.png" markdown>
</div>
<div class="members-description-cell" markdown>
{% if item.web %}<a href="{{ item.web }}" target="_blank">__{{ item.name }}__</a>{% else %}__{{ item.name }}__{% endif %}<br>
{{ item.type }}<br>
{% if item.now %} Now at {{ item.now }} {% endif %}
</div>
</div>
{% endfor %}

</div>


<!--
## Former Undergraduate Students

<div class="grid" markdown>
{% for item in members.former_undergrads %}
<div class="card" markdown>
__{{ item.name }}__
</div>
{% endfor %}
</div>
-->


## Visitors

<div class="grid" markdown>
{% for item in members.visitors %}
<div class="card" markdown>
__{{ item.name }}__<br>
{% if item.period %} {{ item.period }}<br> {% endif %}
{% if item.now %} Now {{ item.now }} {% endif %}
</div>
{% endfor %}
</div>

<br />
