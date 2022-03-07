
<body>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>mermaid.initialize({startOnLoad:true});</script>

 
<p>
Hubs are given tools to transform and validate data. 

Outputted from this is the study metadata, the schema(s) for variable level mappings. Hubs then upload this data to JDC commons.
Training/webinars revolve around using (1) data tool put together to transform/map/validate data (or just validate if they want to do transformations/mappings)
and (2) using the gen3 client and map my files GUIs on JDC. 
        
</p>
</div class="mermaid">

flowchart TB

subgraph Hubs
hub_collect[Collect data via REDCAP,Qualtrics, or other method];
export[Export data in format of choice -- xlsx, spss, csv, etc];
upload_files["Upload export files (data,codebook,publications,filled out templates)\nto JDC using gen3 client"];
map_files["Attach metadata to uploaded files using 'Map my files' tool"];
hub_summary[Fill out the template file\ncontaining subgroup summaries];

hub_collect -- no individual-level\ndata collection --> hub_summary
hub_collect -- individual level\ndata collection --> export 

dasc_synth['synthetic' individual level data from template]
dasc_map[Map and transform variables and values to JDC graph data model];
dasc_output[Output the JDC-transformed dataset to a TSV file];



hub_summary --> dasc_synth --> dasc_map
export --> replace_id["replace local ids with jdc submitter_ids using tool"] --> dasc_map

dasc_map --> dasc_output --> upload_files --> map_files

end

subgraph JCOIN DASC/MAARC
dasc_submit["Submit mapped TSV to JDC graph database (ie sheepdog)"];
map_files --> dasc_submit

jcoin_mds["JCOIN metadata-service"];
heal_mds["HEAL metadata-service"];
subgraph HEAL integration
map_files --> jcoin_mds --> heal_mds;
end
end

<div>    

<p>
Hubs upload de-identified data with associated materials in a format of their convenience and 
then JCOIN DASC does the mapping/transformations and HEAL integration with developed tools

</p>
<div class="mermaid">
    flowchart TB

    subgraph Hubs
    hub_collect[Collect data via REDCAP,Qualtrics, or other method];
    export[Export data in format of choice -- xlsx, spss, csv, etc];
    upload_files["Upload validated data files and metadata (frictionless data package?)\nto JDC using gen3 client"];
    map_files["Attach metadata to uploaded files using 'Map my files' tool"];
    hub_summary[Fill out the template file\ncontaining subgroup summaries];
    
    hub_collect -- no individual-level\ndata collection --> hub_summary
    hub_collect -- individual level\ndata collection --> export 
    
    dasc_synth['synthetic' individual level data from template]
    dasc_map[Map and transform variables and values to JDC graph data model];
    dasc_output[Output the JDC-transformed dataset to a TSV file];
    
    
    
    hub_summary --> dasc_synth --> dasc_map
    export --> replace_id["replace local ids with jdc submitter_ids using tool"] --> dasc_map
    
    dasc_map --> dasc_output --> upload_files --> map_files
    
    end
    
    subgraph JCOIN DASC/MAARC
    dasc_submit["Submit mapped TSV to JDC graph database (ie sheepdog)"];
    map_files --> dasc_submit
    
    jcoin_mds["JCOIN metadata-service"];
    heal_mds["HEAL metadata-service"];
    subgraph HEAL integration
    map_files --> jcoin_mds --> heal_mds;
    end
    end

</div>
  

</body>

