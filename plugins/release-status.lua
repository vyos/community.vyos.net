selector = config["selector"]
path = config["file"]
text = config["text"]

if not selector then
   Log.warning("`selector' must be configured.")
elseif path and text then
   Log.warning("Only one of `path' and `text' can be specified.")
elseif text then
   toml_string = text
elseif path then
   toml_string = Sys.read_file(path)
else
   Log.warning("Either `path' or `text' must be specified.")
end

function generate_table(vyos_version, version_table)
   local target_elem = HTML.select_one(page, selector)
   
   local codename_header = HTML.create_element("h3", vyos_version)
   HTML.set_attribute(codename_header, "id", vyos_version)
   HTML.add_class(codename_header, "version")
   local codename_anchor = HTML.create_element("a")
   HTML.set_attribute(codename_anchor, "href", "#" .. vyos_version)
   HTML.append_child(codename_anchor, codename_header)
   HTML.append_child(target_elem, codename_anchor)

   local version_string = version_table["latest"]
   local version_header = HTML.create_element("h4", version_string)
   HTML.set_attribute(version_header, "id", version_string)
   local version_anchor = HTML.create_element("a")
   HTML.set_attribute(version_anchor, "href", "#" .. version_string)
   HTML.append_child(version_anchor, version_header)
   HTML.append_child(target_elem, version_anchor)

   local notes_string = version_table["notes"]
   if notes_string then
      local notes = HTML.create_element("p", notes_string)
      HTML.append_child(target_elem, notes)
   end

   if not Table.is_empty(version_table["security_advisory"]) then
     Log.debug(JSON.pretty_print(version_table["security_advisory"]))
     local status_table = HTML.create_element("table")
     HTML.append_child(status_table, HTML.parse("<tr><th>CVE</th><th>Name</th><th>Description</th><th>Status</th></tr>"))
      
     local i = 1
     while version_table["security_advisory"][i] do
        local row = version_table["security_advisory"][i]
        local advisory = HTML.create_element("tr")
        HTML.append_child(advisory, HTML.create_element("td", row["cve"]))
        HTML.append_child(advisory, HTML.create_element("td", row["title"]))
        HTML.append_child(advisory, HTML.create_element("td", row["description"]))
        HTML.append_child(advisory, HTML.create_element("td", row["status"]))
        HTML.append_child(status_table, advisory)
        i = i + 1
     end
     HTML.append_child(HTML.select_one(page, selector), status_table)
   end
end

if toml_string then
   local toml_table = TOML.from_string(toml_string)
   Table.iter_ordered(generate_table, toml_table["release"])
end
