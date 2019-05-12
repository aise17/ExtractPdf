import { Component, OnInit } from '@angular/core';

import {Inject} from '@angular/core';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material';


export interface DialogDataError {
  error;
}

@Component({
  selector: 'app-dialog-error',
  templateUrl: './dialog-error.component.html',
  styleUrls: ['./dialog-error.component.css']
})
export class DialogErrorComponent implements OnInit {

  constructor(
    public dialogRef: MatDialogRef<DialogErrorComponent>,
    @Inject(MAT_DIALOG_DATA) public data: DialogDataError) {}

  ngOnInit(){
    console.log(this.data.error)
  }


  onNoClick(): void {
    this.dialogRef.close();
  }

}
