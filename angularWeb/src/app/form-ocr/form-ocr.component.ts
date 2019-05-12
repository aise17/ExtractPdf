import { Component, OnInit, ViewChild } from '@angular/core';
import { saveAs } from 'file-saver/src/FileSaver';
import { Ocr } from '../models/ocr.model';
import { OcrService } from '../services/ocr.service';
import { DialogErrorComponent } from '../dialog-error/dialog-error.component';
import { MatDialog } from '@angular/material';


@Component({
  selector: 'app-form-ocr',
  templateUrl: './form-ocr.component.html',
  styleUrls: ['./form-ocr.component.css']
})
export class FormOcrComponent implements OnInit {

  @ViewChild('fileInput') fileInput;

  formulario: Ocr = new Ocr();
  archivo: string;
  is_progres: boolean;
  ver_form = true;

  constructor(private ser: OcrService, public dialog: MatDialog) { }

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
        orc.usuarioId =  sessionStorage.getItem('id');
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
    const blob = new Blob([this.archivo], {type: 'text/plain;charset=UTF-8'});
    saveAs(blob, 'resultado.docx');
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
