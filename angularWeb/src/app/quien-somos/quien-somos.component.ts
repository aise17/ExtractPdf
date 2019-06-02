import { Component, OnInit } from '@angular/core';
import { QuienSomos } from '../models/quienSomos.model';
import { QuienSomosService } from '../services/quien-somos.service';
import { MatDialog } from '@angular/material';
import { DialogErrorComponent } from '../dialog-error/dialog-error.component';

@Component({
  selector: 'app-quien-somos',
  templateUrl: './quien-somos.component.html',
  styleUrls: ['./quien-somos.component.css']
})
export class QuienSomosComponent implements OnInit {

  public result: QuienSomos;

  constructor(public quienSomosService: QuienSomosService, public dialog: MatDialog) { }

  ngOnInit() {
    this.getContenido();
  }

  getContenido() {
    this.quienSomosService.getContenido()
    .subscribe(res => {
      if(res !== undefined)
      console.log('resultado - >' + res['ok']);
        if (res['ok'] === true){
          this.result = res['salida'][0];
          console.log(this.result)
        }else if(res['ok'] === false){
          this.openDialogError(res['error'])
        }
      else{
        this.openDialogError('error al consegir contenido')
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
