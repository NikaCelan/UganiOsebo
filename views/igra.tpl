% import model
% rebase('base.tpl')

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
    % if stanje == model.ZMAGA:
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
        <tr>
        <td colspan="7"; style="text-align:center;">
        % if igra.stevilo_poskusov != 0:
          % if igra.pravilnost == True:
          <p>Izbrana oseba <u>ima</u> to lastnost.</p>
          % else:
          <p>Izbrana oseba <u>nima</u> te lastnosti.</p>
          % end
        % else:
        <p></p>
        % end
        </td>
        </tr>
      % end
      </td>

    </tr>
</table>
</div>