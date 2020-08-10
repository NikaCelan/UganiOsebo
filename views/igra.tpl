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
        <form action="/igra/"; method="POST">
            <label>Kriterij: </label>
            <select name="vrednost">
          <optgroup label="spol">
            <option value="spol:moški">moški</option>
            <option value="spol:ženska">ženska</option>
          </optgroup>
          <optgroup label="barva las">
            <option value="barva_las:blond">blond</option>
            <option value="barva_las:črna">črna</option>
            <option value="barva_las:rdeča">rdeča</option>
            <option value="barva_las:rjava">rjava</option>
            <option value="barva_las:lasje niso vidni">lasje niso vidni</option>
          </optgroup>
          <optgroup label="dolžina las">
            <option value="dolžina_las:kratki">kratki</option>
            <option value="dolžina_las:dolgi">dolgi</option>
          </optgroup>
          <optgroup label="barva majice">
            <option value="barva_majice:rdeča">rdeča</option>
            <option value="barva_majice:črna">črna</option>
            <option value="barva_majice:siva">siva</option>
            <option value="barva_majice:zelena">zelena</option>
            <option value="barva_majice:bela">bela</option>
            <option value="barva_majice:modra">modra</option>
          </optgroup>
          <optgroup label="usta">
            <option value="usta:odprta">odprta</option>
            <option value="usta:zaprta">zaprta</option>
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