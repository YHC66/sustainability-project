import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SustainabilityListComponent } from './sustainability-list.component';

describe('SustainabilityListComponent', () => {
  let component: SustainabilityListComponent;
  let fixture: ComponentFixture<SustainabilityListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SustainabilityListComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SustainabilityListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
