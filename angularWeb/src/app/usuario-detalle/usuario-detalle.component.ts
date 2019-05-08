import { Component, OnInit, ViewChild } from '@angular/core';
import { UsuarioService } from '../services/usuario.service';
import { Validators, FormControl } from '@angular/forms';
import { Usuario } from '../models/usuario.model';

@Component({
  selector: 'app-usuario-detalle',
  templateUrl: './usuario-detalle.component.html',
  styleUrls: ['./usuario-detalle.component.css']
})
export class UsuarioDetalleComponent implements OnInit {


  public dict: {} = {};

  usuario: Usuario;
  newusuario: Usuario;
  usernameString: string;

  public lineChartLegend = true;
  public lineChartType = 'line';

   // lineChart
   public lineChartData: Array<any> = [
    {data: [], label: 'Peticiones'}
  ];
  public lineChartLabels: Array<any> = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
                                       'Agosto', 'Septiempre', 'Octubre', 'Nobiembre', 'Diciembre'];
  public lineChartOptions: any = {
    responsive: true
  };
  public lineChartColors: Array<any> = [
    { // grey
      backgroundColor: 'rgba(148,159,177,0.2)',
      borderColor: 'rgba(148,159,177,1)',
      pointBackgroundColor: 'rgba(148,159,177,1)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgba(148,159,177,0.8)'
    },
  ];



  @ViewChild('input_user') input_user;
  @ViewChild('input_password') input_password;
  @ViewChild('input_email') input_email;
  @ViewChild('input_nombre') input_nombre;
  @ViewChild('input_apellido') input_apellido;


  emailFormControl = new FormControl('', [
    Validators.required,
    Validators.email
  ]);
  passFormControl = new FormControl('', [
    Validators.required,
  ]);
  constructor(private userService: UsuarioService) {
    this.newusuario = new Usuario();

  }



  // events
  public chartClicked(e: any): void {
    console.log(e);
  }

  public chartHovered(e: any): void {
    console.log(e);
  }

  ngOnInit() {
      this.usuario = new Usuario;
      this.usuario.id = sessionStorage.getItem('id');
      this.usuario.username = sessionStorage.getItem('username');
      this.usuario.password = sessionStorage.getItem('password');
      this.usuario.first_name = sessionStorage.getItem('first_name');
      this.usuario.last_name = sessionStorage.getItem('last_name');
      this.usuario.email = sessionStorage.getItem('email');
      this.getRequest();

  }

  change() {

    console.log( this.newusuario);
    this.newusuario.id = sessionStorage.getItem('id');
    this.userService.change(this.newusuario, sessionStorage.getItem('api_token'))
    .subscribe(res => {
      console.log('salida de cahnge()= ' + res['ok']);
      if (res['ok'] === true ) {
        this.usuario = res['user'];
        console.log('respsuesta' + res);
        console.log('user:' + this.usuario.username);
        sessionStorage.setItem('id', this.usuario.id);
        sessionStorage.setItem('username', this.usuario.username);
        sessionStorage.setItem('password', this.usuario.password);
        sessionStorage.setItem('email', this.usuario.email);
        sessionStorage.setItem('first_name', this.usuario.first_name);
        sessionStorage.setItem('last_name', this.usuario.last_name);
      }
    });
  }

  getRequest() {
    console.log('get request' + this.usuario.id);
    this.userService.getRequest(this.usuario, sessionStorage.getItem('api_token'))
    .subscribe(res => {
       console.log(res);
      this.dict = res;

      for (const key in this.dict) {
        if (this.dict.hasOwnProperty(key)) {
          if (key === 'ok') {
            continue;
          }
          this.lineChartData[0].data.push(this.dict[key]);
        }
      }
    });
  }


}
