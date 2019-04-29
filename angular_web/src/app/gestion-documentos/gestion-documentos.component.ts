import { Component, OnInit, ViewChild } from '@angular/core';
import { UsuarioService } from '../services/usuario.service';
import { Usuario } from '../models/usuario.model';
import { Ocr } from '../models/ocr.model';
import { MatTableDataSource } from '@angular/material/table';
import { SelectionModel } from '@angular/cdk/collections';

import { saveAs } from 'file-saver/src/FileSaver';
import { OcrService } from '../services/ocr.service';
import { JsonOcr } from '../models/JsonOcr.model';
import { MatPaginator } from '@angular/material';

@Component({
  selector: 'app-gestion-documentos',
  templateUrl: './gestion-documentos.component.html',
  styleUrls: ['./gestion-documentos.component.css']
})
export class GestionDocumentosComponent implements OnInit {

  usuario: Usuario;

  files: Ocr[];
  displayedColumns: string[] = ['descripcion', 'documento', 'proceso', 'dateTimeUp', 'select'];
  dataSource = new MatTableDataSource(this.files);

  selection = new SelectionModel<Ocr>(true, []);


  is_progres: boolean;
  ver_form = true;
  archivo: string;

  ruta: string;


  @ViewChild(MatPaginator) paginator: MatPaginator;

  constructor(public userService: UsuarioService, private ser: OcrService) { }

  selected(ocr: JsonOcr) {
    console.log(ocr);
    // this.ruta = ocr.documento;
    // ocr.documento = this.ruta.split('/')[-1];
    console.log(ocr);
    ocr.documento = ocr.documento.split('/', 3)[2];
    ocr.usuario = parseInt(sessionStorage.getItem('id'), 0);
    console.log(ocr.usuario);
    this.send(ocr);
    this.getFiles();

  }


  ngOnInit() {
    this.usuario = new Usuario;
    this.usuario.id = sessionStorage.getItem('id');
    this.usuario.username = sessionStorage.getItem('username');
    this.usuario.password = sessionStorage.getItem('password');
    this.usuario.first_name = sessionStorage.getItem('first_name');
    this.usuario.last_name = sessionStorage.getItem('last_name');
    this.usuario.email = sessionStorage.getItem('email');
    this.getFiles();
  }

  getFiles() {
    this.userService.getFiles(this.usuario)
    .subscribe(res => {
      this.files = res['request'];

      console.log('keys: ' + this.files.keys());
      console.log('files: ' + this.files);
      console.log('res: ' + res['request']);

      this.dataSource = new MatTableDataSource(this.files);
      this.dataSource.paginator = this.paginator;

    });
  }

  aplicarFiltro(filtro: string) {
    this.dataSource.filter = filtro.trim().toLowerCase();
  }

  async send(ocr: JsonOcr) {

    await this.add(ocr);
  }

  add(orc: JsonOcr) {

    if (!orc) {
      console.log('Objeto vacio');
      return;
    }
    this.is_progres = true;


    this.ser.addFileJson( orc )
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


  }

}
