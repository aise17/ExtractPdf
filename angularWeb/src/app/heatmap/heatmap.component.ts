import { Component, OnInit, ViewChild } from '@angular/core';
import { MouseEvent } from '@agm/core';

import { AgmMap, AgmMarker } from '@agm/core';
import { AdminService } from '../services/admin.service';
import { MatDialog } from '@angular/material';
import { DialogErrorComponent } from '../dialog-error/dialog-error.component';
import { IpFile } from '../models/IpFile.model';


@Component({
  selector: 'app-heatmap',
  templateUrl: './heatmap.component.html',
  styleUrls: ['./heatmap.component.css']
})
export class HeatmapComponent implements OnInit {
  

  ipfiles: IpFile [];

  ngOnInit() {
    this.getCoordenadas();
    console.log(this.ipfiles)
  }

  constructor(private adminService: AdminService, public dialog: MatDialog){}
  
  
 // google maps zoom level
 zoom: number = 2;
  
 // initial center position for the map
 lat: number = 40;
 lng: number = 3;

 clickedMarker(label: string, index: number) {
   console.log(`clicked the marker: ${label || index}`)
 }
 
 
 markerDragEnd(m: marker, $event: MouseEvent) {
   console.log('dragEnd', m, $event);
 }
 
 markers: marker[] = [
   {
     lat: 51.673858,
     lng: 7.815982,
     label: 'A',
     draggable: true
   },
   {
     lat: 51.373858,
     lng: 7.215982,
     label: 'B',
     draggable: false
   },
   {
     lat: 51.723858,
     lng: 7.895982,
     label: 'C',
     draggable: true
   }
 ]

  getCoordenadas(){
    this.adminService.getCoordenadas(sessionStorage.getItem('api_token'))
    .subscribe(res => {
      if (res['ok'] === true ) {
        console.log(res['ok']);
        console.log(res['salida']);

        this.ipfiles = res['salida'];
        

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


}

// just an interface for type safety.
interface marker {
 lat: number;
 lng: number;
 label?: string;
 draggable: boolean;
}
