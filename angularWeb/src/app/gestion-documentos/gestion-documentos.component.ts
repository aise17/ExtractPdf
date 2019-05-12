import { Component, OnInit, ViewChild } from '@angular/core';
import { JsonOcr } from '../models/JsonOcr.model';
import { MatTableDataSource, MatPaginator, MatDialog } from '@angular/material';
import { Usuario } from '../models/usuario.model';
import { UsuarioService } from '../services/usuario.service';
import { SelectionModel } from '@angular/cdk/collections';
import { Ocr } from '../models/ocr.model';
import { saveAs } from 'file-saver/src/FileSaver';
import { OcrService } from '../services/ocr.service';
import { DialogErrorComponent } from '../dialog-error/dialog-error.component';


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

  constructor(public userService: UsuarioService, private ser: OcrService, public dialog: MatDialog) { }

  selected(ocr: JsonOcr) {
    console.log(ocr);
    // this.ruta = ocr.documento;
    // ocr.documento = this.ruta.split('/')[-1];
    console.log(ocr);
    ocr.documento = ocr.documento.split('/', 3)[2];
    ocr.usuarioId = sessionStorage.getItem('id');
    console.log(ocr.usuarioId);
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
    this.userService.getFiles(this.usuario, sessionStorage.getItem('api_token'))
    .subscribe(res => {
      if(res['ok'] === true){
      this.files = res['request'];

      console.log('keys: ' + this.files.keys());
      console.log('files: ' + this.files.toString());
      console.log('res: ' + res.fecha_conexion);

      this.dataSource = new MatTableDataSource(this.files);
      this.dataSource.paginator = this.paginator;
      }
      else if(res['ok'] === false){
        this.openDialogError(res['error'])
      }

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
        
    this.ser.addFileJson( orc, sessionStorage.getItem('api_token') )
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
