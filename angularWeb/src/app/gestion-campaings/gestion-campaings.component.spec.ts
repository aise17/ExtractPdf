import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GestionCampaingsComponent } from './gestion-campaings.component';

describe('GestionCampaingsComponent', () => {
  let component: GestionCampaingsComponent;
  let fixture: ComponentFixture<GestionCampaingsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GestionCampaingsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GestionCampaingsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
