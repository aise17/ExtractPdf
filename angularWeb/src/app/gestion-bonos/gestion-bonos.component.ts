import { Component, OnInit, ViewChild } from '@angular/core';
import { DialogErrorComponent } from '../dialog-error/dialog-error.component';
import { Usuario } from '../models/usuario.model';
import { MatTableDataSource, MatPaginator, MatDialog } from '@angular/material';
import { BonoUsuario } from '../models/Bonousuario.model';
import { SelectionModel } from '@angular/cdk/collections';
import { UsuarioService } from '../services/usuario.service';

@Component({
  selector: 'app-gestion-bonos',
  templateUrl: './gestion-bonos.component.html',
  styleUrls: ['./gestion-bonos.component.css']
})
export class GestionBonosComponent implements OnInit {


  usuario: Usuario;

  bonos: BonoUsuario[];
  displayedColumns: string[] = [ 'bono', 'fecha_creacion', 'peticiones_restantes', 'activado'];
  dataSource = new MatTableDataSource(this.bonos);

  selection = new SelectionModel<BonoUsuario>(true, []);


  @ViewChild(MatPaginator) paginator: MatPaginator;

  constructor(public userService: UsuarioService, public dialog: MatDialog) { }

  selected(bono: BonoUsuario) {
    console.log(bono);
  

  }


  ngOnInit() {


    this.getBonos();
  }

  getBonos() {
    let bono = new BonoUsuario();
    bono.usuario = sessionStorage.getItem('id');
    this.userService.getBonos(bono, sessionStorage.getItem('api_token'))
    .subscribe(res => {
      if(res['ok'] === true){
      this.bonos = res['salida'];

      console.log(this.bonos)

      this.dataSource = new MatTableDataSource(this.bonos);
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
