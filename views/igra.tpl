<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
  body, html {
  height: 100%;
  margin: 0;
  }

.bg {
  background-image: url(../img/ozadje.jpg);
  height: 100% ;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
    table {
      margin-left: auto;
      margin-right:auto;
      width: 80%;
    }

    td, th {
    padding: 6px;
}
    h2 {
      color: #ea8b8b;
      font-family: Arial, Helvetica, sans-serif;
      padding-top: 5%;
      font-size: 25px;
      
    }
    label {
        color: #e04d4d;
        font-family: Arial, Helvetica, sans-serif;
        font-size: 18px;
        font-weight:550;
    }
    select {
        color: #e47979;
        font-family: Arial, Helvetica, sans-serif;
        font-size: 15px;
        font-weight:550;

    }
    </style>
  </head>

<body>
  <div class="bg">
<table>
     <caption><h2>UGANI OSEBO</h2></caption>
    <tr>
    <th><img src="../img/0.png" alt="Lena"></th>
    <th><img src="../img/1.png" alt="Vilma"></th>
    <th><img src="../img/2.png" alt="Michael"></th>
    <th><img src="../img/3.png" alt="Robert"></th>
    <th><img src="../img/4.png" alt="Martina"></th>
    <th><img src="../img/5.png" alt="Hans"></th>
    <th><img src="../img/6.png" alt="Hanna"></th>
    </tr>
    <tr>
    <th><img src="../img/7.png" alt="Ludo"></th>
    <th><img src="../img/8.png" alt="Tilman"></th>
    <th><img src="../img/9.png" alt="Ina"></th>
    <th><img src="../img/10.png" alt="Brigitte"></th>
    <th><img src="../img/11.png" alt="Frank"></th>
    <th><img src="../img/12.png" alt="Karl"></th>
    <th><img src="../img/13.png" alt="Erika"></th>
    </tr>
    <tr>
    <td colspan="3"; style="text-align:center;">
        <form action="/igra/"; method="GET">
            <label>Kriterij: </label>
            <select name="vrednost">
          <optgroup label="spol", name="kriterij">
            <option>moški </option>
            <option>ženska </option>
          </optgroup>
          <optgroup label="barva las", name="kriterij">
            <option>blond </option>
            <option>črna </option>
            <option>rdeča </option>
            <option>rjava </option>
            <option>lasje niso vidni </option>
          </optgroup>
          <optgroup label="dolžina las", name="kriterij">
            <option>kratki </option>
            <option>dolgi </option>
          </optgroup>
          <optgroup label="barva majice", name="kriterij">
            <option>rdeča </option>
            <option>črna </option>
            <option>siva </option>
            <option>zelena </option>
            <option>bela </option>
            <option>modra </option>
          </optgroup>
          <optgroup label="usta", name="kriterij">
            <option>odprta </option>
            <option>zaprta </option>
          </optgroup>
            </select>
            
            <button type="submit" name="kriterij"; style="background-color:#ea8b8b; border-color:#C77575; 
            color:white; font-size: 12px; font-family: Arial, Helvetica, 
            sans-serif; padding: 3px;">kriterij</button>
        </form>
      </td>
      
    </tr>
</table>
</div>
</body>

</html>