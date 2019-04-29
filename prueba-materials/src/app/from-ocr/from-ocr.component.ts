import { Component, OnInit, ViewChild } from '@angular/core';
import { Ocr } from '../models/ocr.model';

import {OcrService} from '../services/ocr.service';

import { saveAs } from 'file-saver/src/FileSaver';


@Component({
  selector: 'app-form-ocr',
  templateUrl: './from-ocr.component.html',
  styleUrls: ['./from-ocr.component.css']
})
export class FormOcrComponent implements OnInit {
  @ViewChild('fileInput') fileInput;

  formulario: Ocr = new Ocr();
  archivo: string;
  is_progres: boolean;
  ver_form = true;

  constructor(private ser: OcrService) { }

  ngOnInit() {
  }


  delay(ms: number) {
    return new Promise( resolve => setTimeout(resolve, ms) );
}

  async send() {
    const orc: Ocr = new Ocr();
    const fileBrowser = this.fileInput.nativeElement;
    if (fileBrowser.files && fileBrowser.files[0]) {
      orc.descripcion = this.formulario.descripcion;
      orc.documento = fileBrowser.files[0];
      orc.proceso = this.formulario.proceso;
      if (sessionStorage.getItem('id')) {
        orc.usuario = parseInt( sessionStorage.getItem('id'), 0);
      }

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

    this.ser.addFile( orc )
      .subscribe(res => {
        if (res !== undefined) {
          this.archivo = res['salida'];
          console.log(res['salida']);
          this.saveFile();
          } else {
            console.log('respuesta vacia');
            console.log(res);
          }
      });
    }

  saveFile() {
    const blob = new Blob([this.archivo], {type: 'text/plain;charset=ansi'});
    saveAs(blob, 'resultado.docx');
    this.is_progres = false;
    this.ver_form = true;

  }




}
