---
hide:
  - navigation
  - toc
---


<style>
.people-thumbnail-cell {
    display: inline-table;
    padding-right: 12px;
    vertical-align: top;
    p { margin: 0px; }
}

.people-description-cell {
    display: inline-table;
    vertical-align: top;
    p { margin: 0px; }
}

.people-thumbnail {
    width: 80px;
    border-radius: 50%;
    -moz-background-clip: padding;
    -webkit-background-clip: padding-box;
    background-clip: padding-box
}
</style>


# People

## Professor

<div class="grid" markdown>

{% for item in people.professor %}
<div class="card" markdown>
<div class="people-thumbnail-cell" markdown>
<img class="people-thumbnail" src="../assets/profile/{{ item.name }}.png" markdown>
</div>
<div class="people-description-cell" markdown>
{% if item.link %}
<a href="{{ item.link }}" target="_blank">__{{ item.name }}__</a>
{% else %}
__{{ item.name }}__
{% endif %}

{{ item.type }}

{% if item.email %} <a href="mailto:{{ item.email }}" target="_top">:fontawesome-solid-envelope:</a> {% endif %}
&nbsp;
{% if item.web %} <a href="{{ item.web }}" target="_blank">:fontawesome-solid-house:</a> {% endif %}
</div>
</div>
{% endfor %}

</div>


## Graduate Students

<div class="grid" markdown>

{% for item in people.graduates %}
<div class="card" markdown>
<div class="people-thumbnail-cell" markdown>
<img class="people-thumbnail" src="../assets/profile/{{ item.name }}.png" markdown>
</div>
<div class="people-description-cell" markdown>
{% if item.link %}
<a href="{{ item.link }}" target="_blank">__{{ item.name }}__</a>
{% else %}
__{{ item.name }}__
{% endif %}

{{ item.type }}

{% if item.email %} <a href="mailto:{{ item.email }}" target="_top">:fontawesome-solid-envelope:</a> {% endif %}
&nbsp;
{% if item.web %} <a href="{{ item.web }}" target="_blank">:fontawesome-solid-house:</a> {% endif %}
</div>
</div>
{% endfor %}

</div>


## Undergraduate Students

<div class="grid" markdown>
{% for item in people.undergrads %}
<div class="card" markdown>
__{{ item.name }}__
</div>
{% endfor %}
</div>

## Visitors

<div class="grid" markdown>
{% for item in people.visitors %}
<div class="card" markdown>
__{{ item.name }}__

{% if item.now %} Now {{ item.now }} {% endif %}
</div>
{% endfor %}
</div>


## Alumni (Undergraduate Students)

<div class="grid" markdown>
{% for item in people.alumni_undergrads %}
<div class="card" markdown>
__{{ item.name }}__
</div>
{% endfor %}
</div>


