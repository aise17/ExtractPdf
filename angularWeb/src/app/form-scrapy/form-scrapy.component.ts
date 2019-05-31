import { Component, OnInit, ViewChild } from '@angular/core';
import { DialogErrorComponent } from '../dialog-error/dialog-error.component';
import { saveAs } from 'file-saver/src/FileSaver';
import { Ocr } from '../models/ocr.model';
import { ScrapyService } from '../services/scrapy.service';
import { MatDialog } from '@angular/material';
import { ScrapyFile } from '../models/scrapyFile.model';


@Component({
  selector: 'app-form-scrapy',
  templateUrl: './form-scrapy.component.html',
  styleUrls: ['./form-scrapy.component.css']
})
export class FormScrapyComponent implements OnInit {

  
  @ViewChild('fileInput') fileInput;

  formulario: Ocr = new Ocr();
  archivo: ScrapyFile[];
  is_progres: boolean;
  ver_form = true;

  constructor(private ser: ScrapyService, public dialog: MatDialog) { }

  ngOnInit() {
  }



  async send() {
    const orc: Ocr = new Ocr();
    const fileBrowser = this.fileInput.nativeElement;
    if (fileBrowser.files && fileBrowser.files[0]) {
      orc.descripcion = this.formulario.descripcion;
      orc.documento = fileBrowser.files[0];
      orc.proceso = this.formulario.proceso;
      if (sessionStorage.getItem('id')) {
        orc.usuario =  sessionStorage.getItem('id');
      }
    console.log(orc);
    await this.add(orc);
    }
  }


  add(orc: Ocr) {

    if (!orc) {
      console.log('Objeto vacio');
      return;
    }
    orc.proceso = 'T';
    this.is_progres = true;
    this.ver_form = false;

    this.ser.addFile( orc, sessionStorage.getItem('api_token') )
      .subscribe(res => {
        if (res != undefined){
          if (res['ok'] === true) {
            this.archivo = res['salida'];
            console.log(res);
            this.saveFile();
          } else if(res['ok'] === false) {
            this.openDialogError(res['error'])
          }
        }else{
          this.openDialogError(' [+] error de autentificacion')
          this.is_progres = false;
          this.ver_form = true;
        }
      });
    }

  saveFile() {
    let salida:string;
    salida = "url,alexa,status,platform,language,mail\n"
    this.archivo.forEach(x =>{
      if(x.alexa != null){
        let alexa = x.alexa.replace(RegExp("[*,*]"),".");
        alexa = alexa.replace(RegExp("[*,*]"),".");
        alexa = alexa.replace(RegExp("[*\n*]"),"");
        salida += x.url + "," + alexa + "," + x.status + "," + x.platform  + "," + x.language + "," + x.mail +"\n";
      }else{
        salida += x.url + "," + x.alexa + "," + x.status + "," + x.platform  + "," + x.language + "," + x.mail +"\n";
      }
    })

    const blob = new Blob([salida], {type: 'text/csv;charset=UTF-8'});
    saveAs(blob, 'resultado.csv');
    this.is_progres = false;
    this.ver_form = true;

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
