import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RequestYearEstadisticaAdminComponent } from './request-year-estadistica-admin.component';

describe('RequestYearEstadisticaAdminComponent', () => {
  let component: RequestYearEstadisticaAdminComponent;
  let fixture: ComponentFixture<RequestYearEstadisticaAdminComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RequestYearEstadisticaAdminComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RequestYearEstadisticaAdminComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
