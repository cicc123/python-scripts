import re
str = r'''<td class="ip"><p style='display:none;'></p><span></span><div style='display:inline-block;'></div><span style='display:inline-block;'></span><span style='display:inline-block;'></span><span style='display:inline-block;'>2</span><p style='display:none;'></p><span></span><div style='display:inline-block;'>2</div><span style='display:inline-block;'>3</span><span style='display:inline-block;'></span><p style='display: none;'>.</p><span>.</span><p style='display:none;'>1</p><span>1</span><p style='display:none;'>1</p><span>1</span><span style='display:inline-block;'>1</span><span style='display:inline-block;'>.1</span><p style='display: none;'>31</p><span>31</span><span style='display:inline-block;'>.1</span><p style='display:none;'></p><span></span><span style='display:inline-block;'>00</span>:<span class="port GEGEA">8107</span></td>'''
match = re.sub(r'''<p style='display:none;'>''','',re.sub(r'''\s+:\s+''',':',str))
print(re.findall(r'''<p style='display:none;'>[\d].+?</p>''',str))
print(re.findall(r'''<p style='display:none;'>''',match))
#print(re.findall(r'''<p style='display: none;'>
print(match)