import { Component, OnInit, Inject } from '@angular/core';
import { Usuario } from '../models/usuario.model';
import { Validators, FormControl } from '@angular/forms';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material';
import { DialogData } from '../menu/menu.component';
import { UsuarioService } from '../services/usuario.service';


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
    @Inject(MAT_DIALOG_DATA) public data: DialogData, public userService: UsuarioService) { }

  ngOnInit() {
  }

  registrar(is_register: boolean): void {
    this.register = is_register;
  }



  enviarRegistro() {
    if (!this.emailFormControl.hasError('email') && !this.emailFormControl.hasError('required')) {



      this.userService.register(this.user)
      .subscribe(res => {
        console.log(res);
        if (res['ok'] === true ) {
        this.user = res['user'];
        console.log(res);
        console.log('user:' + this.user.usuario);
        sessionStorage.setItem('id', this.user.id);
        sessionStorage.setItem('username', this.user.usuario);
        sessionStorage.setItem('password', this.user.password);
        sessionStorage.setItem('email', this.user.email);
        sessionStorage.setItem('first_name', this.user.first_name);
        sessionStorage.setItem('last_name', this.user.last_name);



        this.user = new Usuario();
        window.location.href = '/index';
        }
      });


    }
  
  
  
  }

}
