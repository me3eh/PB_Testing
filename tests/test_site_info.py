import pytest
from services.site_info import SiteInfo

@pytest.fixture
def html():
   html = """<div>
          <label class="required" for="id_created_0">
           Created:
          </label>
          <p class="datetime">
           Date:
           <input class="vDateField" id="id_created_0" name="created_0" required="" size="10" type="text" value="17.11.2022"/>
           <br/>
           Time:
           <input class="vTimeField" id="id_created_1" name="created_1" required="" size="8" type="text" value="01:16:18"/>
          </p>
          <input id="initial-id_created_0" name="initial-created_0" type="hidden" value="17.11.2022"/>
          <input id="initial-id_created_1" name="initial-created_1" type="hidden" value="01:16:18"/>
         </div>"""
   return html


@pytest.mark.parametrize("tag, tag_attributes, expected",
                         [("input", None, 4),
                          ("p", None, 1),
                          ("input", {'id': 'initial-id_created_0'}, 1),
                          ("tr", None, 0)
                          ])
def test_get_tag(html, tag, tag_attributes, expected):
    tags = SiteInfo().get_tag(html, tag, tag_attributes=tag_attributes)
    assert len(tags) == expected
