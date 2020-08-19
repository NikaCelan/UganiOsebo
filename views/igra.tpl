<!DOCTYPE html>
<html>
% import model
  <head>
  <title> Ugani Osebo </title>
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
    p {
        font-size: 16px; 
        font-family: Arial, Helvetica, sans-serif; 
        color:#ea8b8b;
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
        padding: 5px;
    }
    </style>
  </head>

<body>
  <div class="bg">
<table>
     <caption><h2>UGANI OSEBO</h2></caption>
    <tr>
    % i = 0
    % while i < 7:
    % if i in model.polje_oseb:
    % slika = "../img/"+str(i)+".png"
    <th><img src="{{slika}}"></th>
    % else:
    % slika = "../img/x"+str(i)+".png"
    <th><img src="{{slika}}"></th>
    % end
    % i = i + 1
    % end
    </tr>
    <tr>
    % i = 7
    % while i <= 13:
    % if i in model.polje_oseb:
    % slika = "../img/"+str(i)+".png"
    <th><img src="{{slika}}"></th>
    % else:
    % slika = "../img/x"+str(i)+".png"
    <th><img src="{{slika}}"></th>
    % end
    % i = i + 1
    % end
    </tr>
    <tr>
    % if len(model.polje_oseb) == 1:
    <td colspan="7"; style="text-align:center;">
    <p>Čestitam. Uspelo ti je. Tvoja oseba je {{ igra.oseba['ime'] }}. Ugotovil si v {{ igra.stevilo_poskusov }} poskusih.</p>

    <form action="/nova-igra/" method="post">
        <button type="submit"; style="background-color:#ea8b8b; border-color:#C77575; 
        color:white; font-size: 16px; font-family: Arial, Helvetica, 
        sans-serif; padding: 5px;">Nova igra</button>
      </form>
    % else:
    <td colspan="3"; style="text-align:center;">
        <form action="/igra/"; method="POST">
            <select name="vrednost">
            %  i = 0
            % (key, val) = model.izdelava_menija[i].split(":")
            % while i < len(model.izdelava_menija):
            % k = key
            <optgroup label="{{k}}">
            % while ((k == key) and (i < len(model.izdelava_menija))):
            <option value="{{model.izdelava_menija[i]}}">{{val}}</option>
            % i = i + 1
            % if i < len(model.izdelava_menija):
            % (key, val) = model.izdelava_menija[i].split(":")
            % end
          % end
        % end
        </optgroup>
        </select>
            <button type="submit" name="kriterij"; style="background-color:#ea8b8b; border-color:#C77575;
            color:white; font-size: 16px; font-family: Arial, Helvetica,
            sans-serif; padding: 5px;">Ugibaj</button>
        </form>
        <td colspan="3"; style="text-align:center;">
          <p>Število poskusov: {{igra.stevilo_poskusov}} </p>
        <td>
      % end
      </td>

    </tr>
</table>
</div>
</body>

</html>