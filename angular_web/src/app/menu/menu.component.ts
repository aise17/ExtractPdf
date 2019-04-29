import { Component, OnInit } from '@angular/core';
import { Usuario } from '../models/usuario.model';


import {MatDialog} from '@angular/material';
import { DialogLoginComponent } from '../dialog-login/dialog-login.component';
import { UsuarioService } from '../services/usuario.service';
import { NONE_TYPE } from '@angular/compiler/src/output/output_ast';



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
export class MenuComponent implements OnInit   {

  user: Usuario ;
  username: string;
  password: string;
  usuario: Usuario;
  constructor(public dialog: MatDialog, private userService: UsuarioService) {
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
        this.user = res['user'];
        console.log(res);
        console.log('user:' + this.user.username);
        sessionStorage.setItem('id', this.user.id);
        sessionStorage.setItem('username', this.user.username);
        sessionStorage.setItem('password', this.user.password);
        sessionStorage.setItem('email', this.user.email);
        sessionStorage.setItem('first_name', this.user.first_name);
        sessionStorage.setItem('last_name', this.user.last_name);
      }
      });
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
      this.user = new Usuario();
      this.user.username = sessionStorage.getItem('username');
      this.user.password = sessionStorage.getItem('password');
    }
  }

}
