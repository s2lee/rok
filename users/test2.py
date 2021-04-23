{% if jprofile.department == '의정부'%}
<h2>Specital Item</h2>
<div class = "col"></div>
<div class = 'col-12 col-xl-8 col-md-4'>
<table class="table">
<tbody>
  <tr>
      <td><a href="#">모든 것을 뚫는 검</a>&nbsp&nbsp{{ item.swordOfGod }}개</td>
      <td><a href="#">모든 것을 뚫는 창</a>&nbsp&nbsp{{ item.spearOfGod }}개</td>
      <td><a href="#">모든 것을 막는 방패</a>&nbsp&nbsp{{ item.shieldOfGod }}개</td>
  </tr>
</tbody>
</table>
</div>
<div class='col'></div>
</div>
{% endif %}

{% if request.user|has_group:"Ranker" %}
  <td><a href="#">탄핵방패</a>&nbsp&nbsp{{ item.impeachment_shield }}개</td>
  <td><a href="#">모든 것을 뚫는 검</a>&nbsp&nbsp{{ item.swordOfGod }}개</td>
  <td><a href="#">모든 것을 뚫는 창</a>&nbsp&nbsp{{ item.spearOfGod }}개</td>
  <td><a href="#">모든 것을 막는 방패</a>&nbsp&nbsp{{ item.shieldOfGod }}개</td>
{% endif %}
