import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NormasOcrComponent } from './normas-ocr.component';

describe('NormasOcrComponent', () => {
  let component: NormasOcrComponent;
  let fixture: ComponentFixture<NormasOcrComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NormasOcrComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NormasOcrComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
