import { Component, OnInit, Inject } from '@angular/core';
import { Usuario } from '../models/usuario.model';
import { Validators, FormControl } from '@angular/forms';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material';
import { DialogData } from '../menu/menu.component';
import { UsuarioService } from '../services/usuario.service';
import { Oauth2Service } from '../services/oauth2.service';


@Component({
  selector: 'app-dialog-login',
  templateUrl: './dialog-login.component.html',
  styleUrls: ['./dialog-login.component.css']
})
export class DialogLoginComponent implements OnInit {

  public register = false;
  user: Usuario = new Usuario();

  emailFormControl = new FormControl('', [
    Validators.required,
    Validators.email
  ]);

  constructor(public dialogRef: MatDialogRef<DialogLoginComponent>,
    @Inject(MAT_DIALOG_DATA) public data: DialogData, public userService: UsuarioService, private oauthService: Oauth2Service) { }

  ngOnInit() {
  }

  registrar(is_register: boolean): void {
    this.register = is_register;
  }



  enviarRegistro() {
    if (!this.emailFormControl.hasError('email') && !this.emailFormControl.hasError('required')) {

      var newuser = new Usuario();

      this.userService.register(this.user)
      .subscribe(res => {
        console.log(res);
        if (res['ok'] === true ) {
        newuser = res['user'];
        console.log(res);
        console.log('user:' + newuser.username);
        sessionStorage.setItem('id', newuser.id);
        sessionStorage.setItem('username', newuser.username);
        sessionStorage.setItem('password', newuser.password);
        sessionStorage.setItem('email', newuser.email);
        sessionStorage.setItem('first_name', newuser.first_name);
        sessionStorage.setItem('last_name', newuser.last_name);

        this.peticionToken(this.user.username, this.user.password);
        }
      }); 
    }
  }

  peticionToken(username: string, password: string) {
    this.oauthService.getToken(username, password)
    .subscribe(res => {

      console.log('peticion de token realizada');
      console.log(res);

      sessionStorage.setItem('api_token', res['access_token']);
      // TODO conseguir que cierre dialogo al cargar api tokenng 
      //window.location.href = '/index';
    });
  }

}
