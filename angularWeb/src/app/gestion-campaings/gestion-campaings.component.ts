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
import { ScrapyService } from '../services/scrapy.service';
import { ScrapyFile } from '../models/scrapyFile.model';
import { AdminService } from '../services/admin.service';
import { Campaing } from '../models/campaing.model';



@Component({
  selector: 'app-gestion-campaings',
  templateUrl: './gestion-campaings.component.html',
  styleUrls: ['./gestion-campaings.component.css']
})
export class GestionCampaingsComponent implements OnInit {


  usuario: Usuario;

  campaings: Campaing[];
 

  constructor(public adminService: AdminService, public dialog: MatDialog) { }

  selected(campaing: Campaing) {
    this.launchCampaing(campaing)
  }


  ngOnInit() {
    this.usuario = new Usuario;
    this.usuario.id = sessionStorage.getItem('id');
    this.usuario.username = sessionStorage.getItem('username');
    this.usuario.password = sessionStorage.getItem('password');
    this.usuario.first_name = sessionStorage.getItem('first_name');
    this.usuario.last_name = sessionStorage.getItem('last_name');
    this.usuario.email = sessionStorage.getItem('email');
    this.usuario.usuario = this.usuario.id;
    this.getCampaings();
  }

  getCampaings() {
    this.adminService.getCampaings(sessionStorage.getItem('api_token'))
    .subscribe(res => {
      if(res !== undefined){
        if(res['ok'] == true){
        this.campaings = res['salida'];
        console.log(this.campaings)
        }
        else if(res['ok'] === false){
          this.openDialogError(res['error'])
        }
      }
    });
  }


  launchCampaing(campaing: Campaing) {
    this.adminService.getLaunchCampaing(campaing, sessionStorage.getItem('api_token'))
    .subscribe(res => {
      if(res !== undefined){
        if(res['ok'] == true){
        console.log('salida ->' + res['ok'])
        }
        else if(res['ok'] === false){
          this.openDialogError(res['error'])
        }
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
