import { Component, OnInit } from '@angular/core';
import { DialogErrorComponent } from '../dialog-error/dialog-error.component';
import { Norma } from '../models/norma.model';
import { Validators, FormBuilder } from '@angular/forms';
import { ContenidoService } from '../services/contenido.service';
import { MatDialog } from '@angular/material';

@Component({
  selector: 'app-normas-scrapy',
  templateUrl: './normas-scrapy.component.html',
  styleUrls: ['./normas-scrapy.component.css']
})
export class NormasScrapyComponent implements OnInit {

  
  isLinear = false;


  constructor(private _formBuilder: FormBuilder, private service: ContenidoService, public dialog: MatDialog) {}

  ngOnInit() {
    this.getNormaScrapy();
  }

  public result: Norma[];


  getNormaScrapy(): void {
    console.log('pulsado');

    this.service.getNormasScrapy()
    .subscribe(res => {
      console.log('resultado - >' + res['ok'])
      if (res['ok'] === true){
        this.result = res['salida'];
        console.log(this.result)
        console.log('Las normas optenidos en la peticion son -> ' + this.result);
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