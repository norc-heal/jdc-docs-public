# Serious Adverse Event Variables

The most up to date information pertaining to a single SAE.  For example, if an SAE is submitted and the a follow up form is submitted with more up to date information, this node will capture the most up to date information. However, all files (ie initial and follow ups will be stored in a child node called serious_adverse_event_files)
Generated through the serious adverse event workflow node


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Variable Name</th>
      <th>Description</th>
      <th>Possible Values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>created_datetime</td>
      <td>A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]</td>
      <td>string<br>null</td>
    </tr>
    <tr>
      <td>gender</td>
      <td>No description</td>
      <td>Female<br>Male<br>Non-binary</td>
    </tr>
    <tr>
      <td>hispanic</td>
      <td>Are you of Hispanic, Latino, or Spanish origin?</td>
      <td>Yes<br>No<br>Not reported</td>
    </tr>
    <tr>
      <td>id</td>
      <td>A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>is_related_to_study</td>
      <td>Is this serious adverse event related to the study?Note,  "Possible" means: There is a reasonable possibility that  the incident, experience, or outcome may have been  caused by the procedures involved in the research.</td>
      <td>None<br>Unlikely<br>Possible<br>Probable<br>Definite</td>
    </tr>
    <tr>
      <td>on_opioid_medication</td>
      <td>Was client taking a medication for opioid use disorder (MOUD)? This is derived from hubs who are are using MOUD intervention.</td>
      <td>Yes<br>No<br>Not reported</td>
    </tr>
    <tr>
      <td>project_id</td>
      <td>Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>protocols.id</td>
      <td>A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>protocols.submitter_id</td>
      <td>No description</td>
      <td>string</td>
    </tr>
    <tr>
      <td>quarter_of_sae</td>
      <td>The quarter and year in which serious adverse event was recorded XXXXqX (e.g., 2020q1 for year 2020, Quarter 1).</td>
      <td>string</td>
    </tr>
    <tr>
      <td>race</td>
      <td>What is your race? SELECT ALL THAT APPLY</td>
      <td>White<br>Black or African American<br>American Indian or Alaska Native (SPECIFY principal tribe or community)<br>Native Hawaiian or Other Pacific Islander<br>Asian<br>Some other race (SPECIFY)<br>Not reported</td>
    </tr>
    <tr>
      <td>state</td>
      <td>The current state of the object.</td>
      <td>uploading<br>uploaded<br>md5summing<br>md5summed<br>validating<br>error<br>invalid<br>suppressed<br>redacted<br>live<br>validated<br>submitted<br>released</td>
    </tr>
    <tr>
      <td>submitter_id</td>
      <td>No description</td>
      <td>string<br>null</td>
    </tr>
    <tr>
      <td>type</td>
      <td>No description</td>
      <td>string</td>
    </tr>
    <tr>
      <td>updated_datetime</td>
      <td>A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]</td>
      <td>string<br>null</td>
    </tr>
    <tr>
      <td>was_expected</td>
      <td>Expected or unexpected? Note, "Unexpected" means unexpected in nature, severity, or frequency given (a) the research procedures that are described in the protocol-related documents  and informed consent document and  (b) the characteristics of the population being studied.</td>
      <td>Expected<br>Unexpected<br>Not reported</td>
    </tr>
  </tbody>
</table>