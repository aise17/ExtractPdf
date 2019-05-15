import { Component, OnInit } from '@angular/core';
import { ContenidoService } from '../services/contenido.service';
import { Bonos } from '../models/bonos.model.';
import { DialogErrorComponent } from '../dialog-error/dialog-error.component';
import { MatDialog } from '@angular/material';
import { BonoUsuario } from '../models/Bonousuario.model';
import { BonoUsuarioService } from '../services/bono-usuario.service';

@Component({
  selector: 'app-bonos',
  templateUrl: './bonos.component.html',
  styleUrls: ['./bonos.component.css']
})
export class BonosComponent implements OnInit {

  constructor(private service: ContenidoService, public dialog: MatDialog, private serviceBonoUsuario: BonoUsuarioService) { }
  public result: Bonos[];

  ngOnInit() {
    this.getBono();
  }

  comprarBono(bono: Bonos){
      console.log('bono comprado -> ' + bono.id);
      let bono_usuario = new BonoUsuario();
      bono_usuario.bono = bono.id
      bono_usuario.usuario = sessionStorage.getItem('id');
      this.serviceBonoUsuario.comprarBono(bono_usuario).subscribe(res => {
            console.log(res);
      });

  }


  getBono(): void {
    console.log('pulsado');

    this.service.getBonos()
    .subscribe(res => {
      console.log('resultado - >' + res['ok'])
      if (res['ok'] === true){
        this.result = res['salida'];
        console.log(this.result)
        console.log('Los bonos optenidos en la peticion son -> ' + this.result);
      }else if(res['ok'] === false){
        this.openDialogError(res['error'])
      }
    }); 
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
