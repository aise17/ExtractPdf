import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material';
import { Usuario } from '../models/usuario.model';
import { DialogLoginComponent } from '../dialog-login/dialog-login.component';
import { UsuarioService } from '../services/usuario.service';
import { Oauth2Service } from '../services/oauth2.service';
import { DialogErrorComponent } from '../dialog-error/dialog-error.component';

export interface DialogData {
  username: string;
  password: string;
  u: Usuario;
}




@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {

  is_admin:boolean;
  user: Usuario ;
  username: string;
  password: string;
  usuario: Usuario;
  constructor(public dialog: MatDialog, private userService: UsuarioService, private oauthService: Oauth2Service) {
  if(sessionStorage.getItem('is_staff')== 'true'){
    this.is_admin = true;
  } 
  }
   openDialog(): void {
    const dialogRef = this.dialog.open(DialogLoginComponent, {
      width: '250px',
      data: {username: this.username, password: this.password}
    });

    dialogRef.afterClosed().subscribe(result => {
      this.username = result[0];
      this.password = result[1];
      this.usuario = new Usuario(this.username, this.password);

      this.userService.login(this.usuario)
      .subscribe(res => {
        if (res['ok'] === true ) {
          console.log(res['ok']);
          console.log(res['salida']);
          this.user = res['salida'];
          this.user.username = res['salida'].username;
          if(this.user.username == 'admin'){
            this.is_admin = true;
          }
          console.log('user:' + this.username);
          sessionStorage.setItem('id', this.user.id);
          sessionStorage.setItem('username', this.user['username']);
          sessionStorage.setItem('password', this.user.password);
          sessionStorage.setItem('email', this.user.email);
          sessionStorage.setItem('first_name', this.user.first_name);
          sessionStorage.setItem('last_name', this.user.last_name);
          sessionStorage.setItem('is_staff', this.user.is_staff);
          console.log('enviando peticion de token')
          this.peticionToken(this.username, this.password);
        }
        else if(res['ok'] === false){
          this.openDialogError(res['error'])
        }
      });
      //window.location.href = '/index';
    });
  
  }

  peticionToken(username: string, password: string) {
    this.oauthService.getToken(username, password)
    .subscribe(res => {

      console.log('peticion de token realizada');
      console.log(res);

      sessionStorage.setItem('api_token', res['access_token']);
    });
  }

  logout(): void {
    console.log('logout()');
    this.userService.logout(this.user)
      .subscribe(res => {
        this.usuario = res;
        console.log(res);
        });
        sessionStorage.clear();
        this.user = null;
  }

  ngOnInit() {
    console.log(sessionStorage.getItem('username'));
    if (sessionStorage.getItem('username') !== null && sessionStorage.getItem('password') !== null) {
      console.log('sesion storage username:' + sessionStorage.getItem('username'));
      this.user = new Usuario()
      this.user.username = sessionStorage.getItem('username');
      this.user.password = sessionStorage.getItem('password');
    }
  }

  openDialogError(request): void {
    const dialogRef = this.dialog.open(DialogErrorComponent, {
      width: '250px',
      data: {error: request}
    });

    dialogRef.afterClosed().subscribe(result => {
     
        console.log('dialogo error cerrado')
      
    });
  
  }

}
