import { Component, OnInit } from '@angular/core';
import { AdminService } from '../services/admin.service';
import { MatDialog } from '@angular/material';
import { DialogErrorComponent } from '../dialog-error/dialog-error.component';
import { BonoUsuario } from '../models/Bonousuario.model';

@Component({
  selector: 'app-compra-bonos-estadistica-admin',
  templateUrl: './compra-bonos-estadistica-admin.component.html',
  styleUrls: ['./compra-bonos-estadistica-admin.component.css']
})
export class CompraBonosEstadisticaAdminComponent implements OnInit {



  public dict: {} = {};

  public lineChartLegend = true;
  public lineChartType = 'line';

   // lineChart
   public lineChartData: Array<any> = [
    {data: [], label: 'Bonos comprados'}
  ];
  public lineChartLabels: Array<any> = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
                                       'Agosto', 'Septiempre', 'Octubre', 'Nobiembre', 'Diciembre'];
  public lineChartOptions: any = {
    responsive: true
  };
  public lineChartColors: Array<any> = [
    { // grey
      backgroundColor: 'rgba(148,159,177,0.2)',
      borderColor: 'rgba(148,159,177,1)',
      pointBackgroundColor: 'rgba(148,159,177,1)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgba(148,159,177,0.8)'
    },
  ];


  constructor(private adminService: AdminService, public dialog: MatDialog){}

  ngOnInit() {
    this.getBonosUsuariobyYear();
    }
    
  // events
  public chartClicked(e: any): void {
    console.log(e);
  }

  public chartHovered(e: any): void {
    console.log(e);
  }




  getBonosUsuariobyYear(){
    this.adminService.getRequesbyYear(sessionStorage.getItem('api_token'))
    .subscribe(res => {
      if(res != undefined){
        if(res['ok'] == true){
          console.log(res)
          this.dict = res;
          for (const key in this.dict) {
            if (this.dict.hasOwnProperty(key)) {
              if (key === 'ok') {
                continue;
              }
              this.lineChartData[0].data.push(this.dict[key]);
            }
          }



        }else{
          this.openDialogError(res['error'])
        }
      }else{
        this.openDialogError('Fallo en la conexion')
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
