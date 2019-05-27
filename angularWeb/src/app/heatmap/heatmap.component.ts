import { Component, OnInit, ViewChild } from '@angular/core';
import { MouseEvent } from '@agm/core';
import { AgmMap, AgmMarker } from '@agm/core';
import { AdminService } from '../services/admin.service';
import { MatDialog, MatTableDataSource, MatPaginator } from '@angular/material';
import { DialogErrorComponent } from '../dialog-error/dialog-error.component';
import { IpFile } from '../models/IpFile.model';
import { SelectionModel } from '@angular/cdk/collections';


@Component({
  selector: 'app-heatmap',
  templateUrl: './heatmap.component.html',
  styleUrls: ['./heatmap.component.css']
})
export class HeatmapComponent implements OnInit {
  

  ipfiles: IpFile [];

  displayedColumns: string[] = ['usuario', 'lat', 'lon'];
  dataSource = new MatTableDataSource(this.ipfiles);

  selection = new SelectionModel<IpFile>(true, []);


  @ViewChild(MatPaginator) paginator: MatPaginator;



  ngOnInit() {
    this.getCoordenadas();
    console.log(this.ipfiles)
  }

  constructor(private adminService: AdminService, public dialog: MatDialog){}
  
  
 // zoom del mapa
 zoom: number = 2;
  
 // posicion inicial del mapa
 lat: number = 40;
 lng: number = 3;

 clickedMarker(label: string, index: number) {
   console.log(`clicked the marker: ${label || index}`)
 }
 
 
 markerDragEnd(m: IpFile, $event: MouseEvent) {
   console.log('dragEnd', m, $event);
 }
 

  getCoordenadas(){
    this.adminService.getCoordenadas(sessionStorage.getItem('api_token'))
    .subscribe(res => {
      if (res['ok'] === true ) {
        console.log(res['ok']);
        console.log(res['salida']);

        this.ipfiles = res['salida'];
        this.dataSource = new MatTableDataSource(this.ipfiles);
        this.dataSource.paginator = this.paginator;
  

      }
      else if(res['ok'] === false){
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

//-----------------------------------

selected(ipfile: IpFile) {
  console.log(ipfile);
}

aplicarFiltro(filtro: string) {
  this.dataSource.filter = filtro.trim().toLowerCase();
}



}

