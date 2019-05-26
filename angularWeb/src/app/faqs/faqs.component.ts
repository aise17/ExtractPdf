import { Component, OnInit } from '@angular/core';
import { ContenidoService } from '../services/contenido.service';
import { MatDialog } from '@angular/material';
import { Faqs } from '../models/faqs.model';
import { DialogErrorComponent } from '../dialog-error/dialog-error.component';

@Component({
  selector: 'app-faqs',
  templateUrl: './faqs.component.html',
  styleUrls: ['./faqs.component.css']
})
export class FaqsComponent implements OnInit {


  constructor(private service: ContenidoService, public dialog: MatDialog) { }
  public result: Faqs[];

  ngOnInit() {
    this.getFaqs();
  }

  getFaqs(): void {
    console.log('pulsado');

    this.service.getFaqs()
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