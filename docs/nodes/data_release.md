# Data Release Variables

Internal node to store different data releases.


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
      <td>id</td>
      <td>A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>major_version</td>
      <td>The number identifying the major version.</td>
      <td>integer</td>
    </tr>
    <tr>
      <td>minor_version</td>
      <td>The number identifying the minor version.</td>
      <td>integer</td>
    </tr>
    <tr>
      <td>name</td>
      <td>String representing release name.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>release_date</td>
      <td>A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]</td>
      <td>string<br>null</td>
    </tr>
    <tr>
      <td>released</td>
      <td>Indicates if it is the current release.</td>
      <td>boolean</td>
    </tr>
    <tr>
      <td>roots.id</td>
      <td>A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>roots.submitter_id</td>
      <td>No description</td>
      <td>string</td>
    </tr>
    <tr>
      <td>type</td>
      <td>No description</td>
      <td>data_release</td>
    </tr>
    <tr>
      <td>updated_datetime</td>
      <td>A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]</td>
      <td>string<br>null</td>
    </tr>
  </tbody>
</table>