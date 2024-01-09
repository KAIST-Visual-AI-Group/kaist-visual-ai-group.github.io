---
hide:
  - navigation
  - toc
---


<style>
.md-typeset .grid {
    grid-template-columns: repeat(auto-fit, minmax(90%, 1fr))
}

.publication-thumbnail-cell {
    display: inline-table;
    padding-right: 12px;
    vertical-align: top;
    p { margin: 0px; }
}

.publication-description-cell {
    display: inline-table;
    vertical-align: top;
    p { margin: 0px; display:inline; line-height: 140%; }
}

.publication-thumbnail {
    width: 160px;
    border-radius: 8px;
    -moz-background-clip: padding;
    -webkit-background-clip: padding-box;
    background-clip: padding-box
}
</style>


# Publications

<div class="grid" markdown>

{% for paper in publications %}
<div class="card" markdown>
<div class="publication-thumbnail-cell" markdown>
<img class="publication-thumbnail" src="../assets/thumbnails/{{ paper.key }}-thumbnail.png" markdown>
</div>
<div class="publication-description-cell" markdown>
__{{ paper.title }}__<br>
{% for author in paper.authors %}{% if author.name == people.professor.name %}<a href="{{ people.professor.web }}" target=_blank>{{ author.name }}</a>{% elif author.name == people.professor.legacy_name %}<a href="{{ people.professor.web }}" target=_blank>{{ author.name }}</a>{% elif author.link %}<a href="{{ author.link }}" target=_blank>{{ author.name }}</a>{% else %}{{ author.name }}{% endif %}&ensp;{% endfor %}{% if paper.authors_note %}(\* {{ paper.authors_note }}){% endif %}<br>
{{ paper.venue }} {{ paper.year }} {% if paper.publication_note %}__({{ paper.publication_note }})__{% endif %}<br>
{% if paper.project %} <a href="{{ paper.project }}" target=_blank>Project</a>&ensp;{% endif %}{% if paper.arXiv %} <a href="{{ paper.arXiv }}" target=_blank>arXiv</a>&ensp;{% endif %}{% if paper.pdf %} <a href="{{ paper.pdf }}" target=_blank>PDF</a>&ensp;{% endif %}{% if paper.slides %} <a href="{{ paper.slides }}" target=_blank>Slides</a>&ensp;{% endif %}{% if paper.poster %} <a href="{{ paper.poster }}" target=_blank>Poster</a>&ensp;{% endif %}{% if paper.video %} <a href="{{ paper.video }}" target=_blank>Video</a>&ensp;{% endif %}{% if paper.web_demo %} <a href="{{ paper.web_demo }}" target=_blank>Web Demo</a>&ensp;{% endif %}{% if paper.supplementary %}<a href="{{ paper.supplementary }}" target=_blank>Supplementary</a>&ensp{% endif %}{% if paper.code %}<a href="{{ paper.code }}" target=_blank>Code</a>&ensp;{% endif %}{% if paper.hugging_face %}<a href="{{ paper.hugging_face }}" target=_blank>Hugging Face</a>&ensp;{% endif %}{% if paper.press_release %}{% for press_release in paper.press_release %}<a href="{{ press_release.link }}" target=_blank>Media {{ loop.index }}</a>&ensp;{% endfor %}{% endif %}
</div>
</div>
{% endfor %}

</div>


