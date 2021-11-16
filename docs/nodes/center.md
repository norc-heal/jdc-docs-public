# Center Variables

Genetic Research Center (GRC) or other clinical center at which research participants are recruited.


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
      <td>follow_ups.id</td>
      <td>A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>follow_ups.submitter_id</td>
      <td>No description</td>
      <td>string</td>
    </tr>
    <tr>
      <td>genhl</td>
      <td>Subject perception about his current health.</td>
      <td>Excellent<br>Very Good<br>Good<br>Fair<br>Poor</td>
    </tr>
    <tr>
      <td>id</td>
      <td>A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>project_id</td>
      <td>Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>state</td>
      <td>The current state of the object.</td>
      <td>uploading<br>uploaded<br>md5summing<br>md5summed<br>validating<br>error<br>invalid<br>suppressed<br>redacted<br>live<br>validated<br>submitted<br>released</td>
    </tr>
    <tr>
      <td>submitter_id</td>
      <td>A project-specific identifier for a node. This property is the calling card/nickname/alias for a unit of submission. It can be used in place of the UUID for identifying or recalling a node.</td>
      <td>string</td>
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
  </tbody>
</table>