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

  public contenido: QuienSomos;

  constructor(public quienSomosService: QuienSomosService, public dialog: MatDialog) { }

  ngOnInit() {
    this.getContenido();
  }

  getContenido() {
    this.quienSomosService.getContenido()
    .subscribe(res => {
      console.log(res);
      this.contenido = res[0];
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
